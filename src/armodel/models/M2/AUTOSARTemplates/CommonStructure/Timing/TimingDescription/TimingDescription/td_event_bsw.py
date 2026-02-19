"""TDEventBsw AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 251)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)
from abc import ABC, abstractmethod


class TDEventBsw(TimingDescriptionEvent, ABC):
    """AUTOSAR TDEventBsw."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    bsw_module_description: Optional[BswModuleDescription]
    def __init__(self) -> None:
        """Initialize TDEventBsw."""
        super().__init__()
        self.bsw_module_description: Optional[BswModuleDescription] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventBsw to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBsw, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_description
        if self.bsw_module_description is not None:
            serialized = ARObject._serialize_item(self.bsw_module_description, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-DESCRIPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBsw":
        """Deserialize XML element to TDEventBsw object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBsw object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBsw, cls).deserialize(element)

        # Parse bsw_module_description
        child = ARObject._find_child_element(element, "BSW-MODULE-DESCRIPTION")
        if child is not None:
            bsw_module_description_value = ARObject._deserialize_by_tag(child, "BswModuleDescription")
            obj.bsw_module_description = bsw_module_description_value

        return obj



class TDEventBswBuilder:
    """Builder for TDEventBsw."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBsw = TDEventBsw()

    def build(self) -> TDEventBsw:
        """Build and return TDEventBsw object.

        Returns:
            TDEventBsw instance
        """
        # TODO: Add validation
        return self._obj
