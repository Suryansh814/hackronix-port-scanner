import xml.etree.ElementTree as ET


class NmapParser:

    @staticmethod
    def parse(xml_output: str):

        root = ET.fromstring(xml_output)

        result = {
            "host": None,
            "status": None,
            "ports": []
        }

        host = root.find("host")

        if host is None:
            return result

        address = host.find("address")

        if address is not None:
            result["host"] = address.attrib.get("addr")

        status = host.find("status")

        if status is not None:
            result["status"] = status.attrib.get("state")

        ports = host.find("ports")

        if ports is None:
            return result

        for port in ports.findall("port"):

            service = port.find("service")

            state = port.find("state")

            result["ports"].append({

                "port": int(port.attrib["portid"]),

                "protocol": port.attrib["protocol"],

                "state": state.attrib["state"],

                "service": service.attrib.get("name", "")
            })

        return result
