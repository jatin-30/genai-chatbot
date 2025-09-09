from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.index import LocalIndex
encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
         # Return policy
        "What is the return policy of the products?",
        "How can I return an item?",
        "In how many days can I return a product?",
        "Can I return something if I don't like it?",
        "Do you allow free returns?",

        # Discounts (HDFC)
        "Do I get discount with the HDFC credit card?",
        "Is there an offer for HDFC credit card users?",
        "How much discount do I get with HDFC card?",
        "Do you have HDFC card promotions?",
        "Does HDFC credit card give cashback here?",

        # Order tracking
        "How can I track my order?",
        "Where is my order?",
        "Can you help me with the tracking link?",
        "How do I know the status of my order?",
        "When will my package arrive?",

        # Payment methods
        "What payment methods are accepted?",
        "Do you accept UPI?",
        "Can I pay with credit or debit card?",
        "Do you have cash on delivery?",
        "What payment options are available?",

        # Refund process
        "How long does it take to process a refund?",
        "When will I get my money back?",
        "How much time does a refund take?",
        "Do refunds take more than a week?",
        "Tell me about refund timelines.",

        # Sales and promotions
        "Are there any ongoing sales or promotions?",
        "Do you have any current offers?",
        "Where can I see discounts?",
        "Any items on sale right now?",
        "Show me your ongoing deals.",

        # Cancel or modify orders
        "Can I cancel or modify my order after placing it?",
        "Is it possible to change my order?",
        "Can I edit my order after checkout?",
        "How do I cancel an order?",
        "Can I update my order details?",

        # International shipping
        "Do you offer international shipping?",
        "Can you ship outside India?",
        "Is international delivery available?",
        "Do you send products abroad?",
        "Can I place an order from another country?",

        # Damaged product
        "What should I do if I receive a damaged product?",
        "My product arrived defective, what now?",
        "What happens if I get a broken item?",
        "How do I report a damaged delivery?",
        "Do you replace faulty products?",

        # Promo code
        "How do I use a promo code during checkout?",
        "Where can I enter a discount code?",
        "How do I apply a coupon?",
        "Can I use promo codes on sale items?",
        "How to redeem an offer code?"
    ]
)

sql = Route(
    name='sql',
    utterances=[
         # Brand + discount
        "I want to buy Nike shoes that have 50% discount",
        "Show me Adidas shoes on sale",
        "Do you have Puma sneakers with a discount?",
        "List Reebok shoes under offer",
        "Any Woodland shoes available at 30% off?",

        # Price-based queries
        "Are there any shoes under Rs. 3000?",
        "Show me shoes priced below 2000",
        "List shoes between 4000 and 6000 rupees",
        "Which shoes are the cheapest?",
        "Do you have luxury shoes above Rs. 10,000?",

        # Category-specific
        "Do you have formal shoes in size 9?",
        "Show me casual sneakers for men",
        "I’m looking for women’s running shoes",
        "Any leather formal shoes available?",
        "Display sports shoes for gym use",

        # Size-based queries
        "Do you have shoes in size 8?",
        "Which brands have size 10 sneakers?",
        "Are there any sandals in size 7?",
        "Show me boots in size 9",

        # Color-based queries
        "Do you have white sneakers?",
        "List black running shoes",
        "Are there red Puma shoes?",
        "Any blue Adidas shoes in stock?",

        # Price + brand + category combos
        "What is the price of Puma running shoes?",
        "Show me Nike sneakers under Rs. 5000",
        "Adidas shoes between 2000 and 4000 rupees",
        "Do you have Bata formal shoes under 1500?",
        "Find Woodland trekking shoes below Rs. 6000",

        # Availability queries
        "Which shoes are currently in stock?",
        "Do you have the latest arrivals from Nike?",
        "Are Adidas Ultraboost available?",
        "Show me trending sneakers right now",
        "Any shoes available for next-day delivery?"
    ]
)

index = LocalIndex()
router = SemanticRouter(routes=[faq, sql], encoder=encoder, index=index)
router.sync(sync_mode="local")

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)