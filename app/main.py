import asyncio

async def handle_client(reader, writer):
    """
    Handles a single client connection.
    """
    print("Accepted connection!")
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break  # Client disconnected
            writer.write(b"+PONG\r\n")
            await writer.drain()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
        print("Connection closed")

async def main():
    """
    Main server logic to accept multiple connections concurrently.
    """
    server = await asyncio.start_server(handle_client, "localhost", 6379)
    async with server:
        print("Server started on localhost:6379")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())