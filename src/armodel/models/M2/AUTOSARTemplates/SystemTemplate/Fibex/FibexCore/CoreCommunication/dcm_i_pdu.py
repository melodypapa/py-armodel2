"""DcmIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DiagPduType,
)


class DcmIPdu(IPdu):
    """AUTOSAR DcmIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diag_pdu_type: Optional[DiagPduType]
    def __init__(self) -> None:
        """Initialize DcmIPdu."""
        super().__init__()
        self.diag_pdu_type: Optional[DiagPduType] = None

    def serialize(self) -> ET.Element:
        """Serialize DcmIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DcmIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diag_pdu_type
        if self.diag_pdu_type is not None:
            serialized = ARObject._serialize_item(self.diag_pdu_type, "DiagPduType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-PDU-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DcmIPdu":
        """Deserialize XML element to DcmIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DcmIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DcmIPdu, cls).deserialize(element)

        # Parse diag_pdu_type
        child = ARObject._find_child_element(element, "DIAG-PDU-TYPE")
        if child is not None:
            diag_pdu_type_value = DiagPduType.deserialize(child)
            obj.diag_pdu_type = diag_pdu_type_value

        return obj



class DcmIPduBuilder:
    """Builder for DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DcmIPdu = DcmIPdu()

    def build(self) -> DcmIPdu:
        """Build and return DcmIPdu object.

        Returns:
            DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
