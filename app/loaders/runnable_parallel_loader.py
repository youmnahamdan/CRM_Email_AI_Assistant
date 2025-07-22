from langchain_core.runnables import Runnable, RunnableParallel

def load_runnable_parallel(
    number_of_replies: int,
    suggestion_chain: Runnable
):

    # Create dictionary of (reply: chain)
    replies_dict = {
        f'Reply {i+1}': suggestion_chain
        for i in range(number_of_replies)
    }
    
    # Parallel runnable
    runnable = RunnableParallel(**replies_dict)

    return runnable