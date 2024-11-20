const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Express app setup
const app = express();
app.use(bodyParser.json());
app.use(cors());

// MongoDB connection
mongoose.connect(
  'mongodb+srv://umeshwar:123@cluster0.msbqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }
)
  .then(() => console.log('MongoDB connected successfully...'))
  .catch(err => console.error(err));

// Goal Model
const Goal = mongoose.model('Goals', {
  text: String,
});

// Routes

// GET: Fetch all goals
app.get('/restapi/goals', async (req, res) => {
  const goals = await Goal.find();
  console.log(goals);
  res.json(goals);
});

// POST: Add a new goal
app.post('/restapi/goals', async (req, res) => {
  const goal = new Goal({ text: req.body.text });
  await goal.save();
  res.json(goal);
});

// PUT: Update a goal by ID
app.put('/restapi/goals/:id', async (req, res) => {
  const { id } = req.params;
  const { text } = req.body;

  try {
    const updatedGoal = await Goal.findByIdAndUpdate(
      id,
      { text },
      { new: true, runValidators: true }
    );

    if (!updatedGoal) {
      return res.status(404).json({ message: 'Goal not found' });
    }

    res.json(updatedGoal);
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while updating the goal' });
  }
});

// DELETE: Delete a goal by ID
app.delete('/restapi/goals/:id', async (req, res) => {
  const { id } = req.params;

  try {
    const deletedGoal = await Goal.findByIdAndDelete(id);

    if (!deletedGoal) {
      return res.status(404).json({ message: 'Goal not found' });
    }

    res.json({ message: 'Goal deleted', deletedGoal });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while deleting the goal' });
  }
});

// Start server
app.listen(5000, () => {
  console.log('Server running on http://localhost:5000');
});
