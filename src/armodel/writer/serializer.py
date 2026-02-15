"""Python object to XML serialization."""

from lxml import etree
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR


def serialize_autosar_to_xml(autosar: AUTOSAR) -> etree.Element:
    """Serialize AUTOSAR object to XML element.

    Args:
        autosar: AUTOSAR object to serialize

    Returns:
        Root XML element
    """
    # Call object's serialize method
    root = autosar.serialize()
    return root

