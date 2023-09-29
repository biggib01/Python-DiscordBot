import bot
import testRun

if __name__ == '__main__':
    testRun.bot.run(
        asyncio_debug=True,             # enable asyncio debug to detect blocking and slow code.

        coroutine_tracking_depth=20,    # enable tracking of coroutines, makes some asyncio
                                        # errors clearer.
        propagate_interrupts=True,      # any OS interrupts get rethrown as an errors.
    )