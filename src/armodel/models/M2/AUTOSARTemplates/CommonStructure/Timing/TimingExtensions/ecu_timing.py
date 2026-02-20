"""EcuTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 30)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_value_collection import (
    EcucValueCollection,
)


class EcuTiming(TimingExtension):
    """AUTOSAR EcuTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcuTiming."""
        super().__init__()
        self.ecu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcuTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_ref
        if self.ecu_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_ref, "EcucValueCollection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuTiming":
        """Deserialize XML element to EcuTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuTiming, cls).deserialize(element)

        # Parse ecu_ref
        child = ARObject._find_child_element(element, "ECU-REF")
        if child is not None:
            ecu_ref_value = ARRef.deserialize(child)
            obj.ecu_ref = ecu_ref_value

        return obj



class EcuTimingBuilder:
    """Builder for EcuTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuTiming = EcuTiming()

    def build(self) -> EcuTiming:
        """Build and return EcuTiming object.

        Returns:
            EcuTiming instance
        """
        # TODO: Add validation
        return self._obj
