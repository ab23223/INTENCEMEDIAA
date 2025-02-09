const express = require('express');
const stripe = require('stripe')('sk_test_51QqjkZBFp1gEAbUcPkQCwFqshbmOUu44YcCNhmZkazZCZXzPqvwTpyhg7XpPN5xTcILhtmCmjEqqIyK0BmAq2L8t00ROYmPFvQ'); // Replace with your secret Stripe key
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Endpoint to handle payment processing
app.post('/create-charge', async (req, res) => {
    const { token, packageName, packagePrice, gst, total } = req.body;

    try {
        // Create a charge with Stripe
        const charge = await stripe.charges.create({
            amount: total * 100, // Total in cents
            currency: 'usd',
            description: packageName,
            source: token,
            metadata: {
                packageName: packageName,
                packagePrice: packagePrice,
                gst: gst,
                total: total
            }
        });

        // If the charge is successful, send success response
        res.json({ success: true });
    } catch (error) {
        // Handle error
        console.error(error);
        res.json({ success: false, message: error.message });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
