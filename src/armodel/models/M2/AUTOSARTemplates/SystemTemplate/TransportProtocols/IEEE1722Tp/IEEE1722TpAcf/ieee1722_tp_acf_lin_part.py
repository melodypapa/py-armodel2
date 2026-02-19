"""IEEE1722TpAcfLinPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 667)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfLinPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lin_identifier: Optional[PositiveInteger]
    sdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLinPart."""
        super().__init__()
        self.lin_identifier: Optional[PositiveInteger] = None
        self.sdu_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfLinPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfLinPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lin_identifier
        if self.lin_identifier is not None:
            serialized = ARObject._serialize_item(self.lin_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_ref
        if self.sdu_ref is not None:
            serialized = ARObject._serialize_item(self.sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLinPart":
        """Deserialize XML element to IEEE1722TpAcfLinPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfLinPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfLinPart, cls).deserialize(element)

        # Parse lin_identifier
        child = ARObject._find_child_element(element, "LIN-IDENTIFIER")
        if child is not None:
            lin_identifier_value = child.text
            obj.lin_identifier = lin_identifier_value

        # Parse sdu_ref
        child = ARObject._find_child_element(element, "SDU-REF")
        if child is not None:
            sdu_ref_value = ARRef.deserialize(child)
            obj.sdu_ref = sdu_ref_value

        return obj



class IEEE1722TpAcfLinPartBuilder:
    """Builder for IEEE1722TpAcfLinPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfLinPart = IEEE1722TpAcfLinPart()

    def build(self) -> IEEE1722TpAcfLinPart:
        """Build and return IEEE1722TpAcfLinPart object.

        Returns:
            IEEE1722TpAcfLinPart instance
        """
        # TODO: Add validation
        return self._obj
