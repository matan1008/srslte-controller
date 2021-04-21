from pyshark import FileCapture

from srslte_controller.uu_events.nas_emm_attach_request import create as create_attach_request

ATTACH_REQUEST_PCAP_DATA = (
    'd4c3b2a1020004000000000000000000ffff0000930000000849796091c70b00180200001802000001000302004603000004026807010a00'
    '0f00013a3e211f1f35000000a0000020002a0e82e2101220202064a8ed3005e0e000080403a0220000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    '00000000000000000000000000000000'
)


def test_parsing_emm_attach_request(tmp_path):
    p = tmp_path / 'attach_request.pcap'
    p.write_bytes(bytes.fromhex(ATTACH_REQUEST_PCAP_DATA))
    pcap = FileCapture(str(p))
    rar = create_attach_request(list(pcap)[0])
    assert rar == {'imsi': '001010123456789', 'event': 'Attach request', 'rnti': 70}