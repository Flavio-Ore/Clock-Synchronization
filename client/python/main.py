import asyncio
import datetime
import socket
from timeit import default_timer

from dateutil import parser

SERVER_ADDRESS = "192.168.1.44"
SERVER_PORT = 3333
running = True


async def stop_tread():
    """
    Stop the client when any key is pressed.
    """
    global running
    print("-----------------------------------")
    await asyncio.get_event_loop().run_in_executor(
        None,
        input,
        "Press any key to stop the client.\n-----------------------------------\n",
    )
    running = False


async def synchronize_time():
    """
    **Christian's Algorithm.**
    The client requests the server for the current time and calculates the process delay latency.
    """
    while running:
        print("\nCreating socket and connecting to server...")
        await asyncio.sleep(1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_ADDRESS, SERVER_PORT))
            request_time = default_timer()

            server_time = parser.parse(sock.recv(1024, 0).decode())
            response_time = default_timer()
            actual_time = datetime.datetime.now()
            process_delay_latency = response_time - request_time

            print("Time returned by server: " + str(server_time))
            print("Process Delay latency: " + str(process_delay_latency) + " seconds")
            print("Actual clock time at client side: " + str(actual_time))

            #! synchronize process client clock time
            client_time = server_time + datetime.timedelta(
                seconds=(process_delay_latency) / 2
            )

            print("Synchronized process client time: " + str(client_time))

            # calculate synchronization error
            error = actual_time - client_time
            print("Synchronization error : " + str(error.total_seconds()) + " seconds")
            sock.close()


async def main() -> None:
    """
    The main function to run the client.
    """
    stop_program = asyncio.create_task(stop_tread())
    christian_algorithm = asyncio.create_task(synchronize_time())
    await stop_program
    await christian_algorithm
    print("Client stopped.")


if __name__ == "__main__":
    asyncio.run(main())
