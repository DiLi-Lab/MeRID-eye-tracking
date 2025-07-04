import argparse
import os

from gooey import Gooey
from gooey import GooeyParser

from experiment.participant_questionnaire import MeRIDParticipantQuestionnaire
import constants


def run_pq_only(id: int, session: int) -> None:
    participant_id_str = str(id)

    # participant id should always be 3 digits long
    while len(participant_id_str) < 3:
        participant_id_str = "0" + participant_id_str

    # create res folder
    repo_root = constants.EXP_ROOT_PATH
    os.makedirs(f'{repo_root.parent}/test_pq', exist_ok=True)

    pq = MeRIDParticipantQuestionnaire(participant_id, f'{repo_root.parent}/test_pq', session_id=session)
    pq.run_questionnaire()


@Gooey(
    program_name='Test MeRID Participant Questionnaire',
)
def parse_args():
    gooey_parser = GooeyParser(
        description='Run the MeRID participant questionnaire without the experiment.',
    )

    gooey_parser.add_argument(
        '--participant_id',
        metavar='Participant ID',
        type=int,
        default=1,
        help='The ID of the participant. Default is 1.',

    )

    gooey_parser.add_argument(
        '--session-id',
        metavar='Session ID',
        type=int,
        default=1,
        choices=[1, 2],
        help='The session ID for the participant. Default is 1.',
    )

    return gooey_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    participant_id = args.participant_id
    session_id = args.session_id

    run_pq_only(participant_id, session_id)
