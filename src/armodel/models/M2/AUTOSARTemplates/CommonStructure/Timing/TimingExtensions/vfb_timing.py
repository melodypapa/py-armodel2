"""VfbTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 24)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class VfbTiming(TimingExtension):
    """AUTOSAR VfbTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    component_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize VfbTiming."""
        super().__init__()
        self.component_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize VfbTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VfbTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component_ref
        if self.component_ref is not None:
            serialized = ARObject._serialize_item(self.component_ref, "SwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPONENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VfbTiming":
        """Deserialize XML element to VfbTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VfbTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VfbTiming, cls).deserialize(element)

        # Parse component_ref
        child = ARObject._find_child_element(element, "COMPONENT-REF")
        if child is not None:
            component_ref_value = ARRef.deserialize(child)
            obj.component_ref = component_ref_value

        return obj



class VfbTimingBuilder:
    """Builder for VfbTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VfbTiming = VfbTiming()

    def build(self) -> VfbTiming:
        """Build and return VfbTiming object.

        Returns:
            VfbTiming instance
        """
        # TODO: Add validation
        return self._obj
