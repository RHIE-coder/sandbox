import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os
from dotenv import load_dotenv

load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.getenv('SPREAD_SHEET_ID')
SAMPLE_RANGE_NAME = "A11:Q500"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    print(dir(sheet))

    print()
    print()
    print()
    print('------------------')

    # 스프레드시트의 메타데이터 가져오기
    sheet_metadata = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()
    print(sheet_metadata)
    print()
    print()
    print()
    print('------------------')

    # 스프레드시트 내의 시트 리스트 가져오기
    sheets = sheet_metadata.get('sheets', [])

    # 각 시트의 이름 출력
    sheet_names = [sheet['properties'] for sheet in sheets]
    print("Sheet names in the spreadsheet:")
    for name in sheet_names:
        print(name)
    print()
    print()
    print()
    print('------------------')

    for name in sheet_names:
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=name['title'])
            .execute()
        )
        values = result.get("values", [])
        for row in values:
            print(row)
        print()
        print()
        print()
        print('------------------')

    print()
    print()
    print()
    print('------------------')
    os.exit()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    for row in values:
      print(row)
      # Print columns A and E, which correspond to indices 0 and 4.
    #   print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()