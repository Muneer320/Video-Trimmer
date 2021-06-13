from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def main():
    filename = input("Video location with filename: ")
    if '.' not in filename:
        print("Please include the video filename in location as well")
        filename = input("Video location with filename: ")

    start = int(input("Start time of the result: "))
    end = int(input("End time of the result: "))
    result = input("Output Name:")
    if result == "":
        result = "result.mp4"

    ffmpeg_extract_subclip(filename, start, end, targetname=result)

    print("\nSuccessfully trimmer the video.")


if __name__ == "__main__":
    main()