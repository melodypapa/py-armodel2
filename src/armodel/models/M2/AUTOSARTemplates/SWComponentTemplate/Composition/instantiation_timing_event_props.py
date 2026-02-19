"""InstantiationTimingEventProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class InstantiationTimingEventProps(InstantiationRTEEventProps):
    """AUTOSAR InstantiationTimingEventProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize InstantiationTimingEventProps."""
        super().__init__()
        self.period: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize InstantiationTimingEventProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InstantiationTimingEventProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize period
        if self.period is not None:
            serialized = ARObject._serialize_item(self.period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationTimingEventProps":
        """Deserialize XML element to InstantiationTimingEventProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InstantiationTimingEventProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InstantiationTimingEventProps, cls).deserialize(element)

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        return obj



class InstantiationTimingEventPropsBuilder:
    """Builder for InstantiationTimingEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationTimingEventProps = InstantiationTimingEventProps()

    def build(self) -> InstantiationTimingEventProps:
        """Build and return InstantiationTimingEventProps object.

        Returns:
            InstantiationTimingEventProps instance
        """
        # TODO: Add validation
        return self._obj
