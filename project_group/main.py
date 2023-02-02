import overheads, cash_on_hand, profit_loss

# Create a funtion 'main()' which consolidates all sub functions
def main():

    # Run overheads_function() to write report
    overheads.overheads_function()

    # Run coh_difference() to write report
    cash_on_hand.coh_difference()
    
    # Run profitloss.difference() to write report
    profit_loss.profitloss_difference()

    
# Run main function to activate the programme
main()
