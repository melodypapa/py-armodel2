"""StaticPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 410)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
    MultiplexedPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class StaticPart(MultiplexedPart):
    """AUTOSAR StaticPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize StaticPart."""
        super().__init__()
        self.i_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize StaticPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StaticPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = ARObject._serialize_item(self.i_pdu_ref, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StaticPart":
        """Deserialize XML element to StaticPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StaticPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StaticPart, cls).deserialize(element)

        # Parse i_pdu_ref
        child = ARObject._find_child_element(element, "I-PDU-REF")
        if child is not None:
            i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_pdu_ref = i_pdu_ref_value

        return obj



class StaticPartBuilder:
    """Builder for StaticPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StaticPart = StaticPart()

    def build(self) -> StaticPart:
        """Build and return StaticPart object.

        Returns:
            StaticPart instance
        """
        # TODO: Add validation
        return self._obj
