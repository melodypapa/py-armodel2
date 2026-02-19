"""TDEventBswInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """AUTOSAR TDEventBswInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_entity_entity: Optional[BswModuleEntity]
    td_event_bsw_behavior_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventBswInternalBehavior."""
        super().__init__()
        self.bsw_module_entity_entity: Optional[BswModuleEntity] = None
        self.td_event_bsw_behavior_type: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventBswInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBswInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_entity_entity
        if self.bsw_module_entity_entity is not None:
            serialized = ARObject._serialize_item(self.bsw_module_entity_entity, "BswModuleEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-ENTITY-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_bsw_behavior_type
        if self.td_event_bsw_behavior_type is not None:
            serialized = ARObject._serialize_item(self.td_event_bsw_behavior_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-BSW-BEHAVIOR-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswInternalBehavior":
        """Deserialize XML element to TDEventBswInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswInternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBswInternalBehavior, cls).deserialize(element)

        # Parse bsw_module_entity_entity
        child = ARObject._find_child_element(element, "BSW-MODULE-ENTITY-ENTITY")
        if child is not None:
            bsw_module_entity_entity_value = ARObject._deserialize_by_tag(child, "BswModuleEntity")
            obj.bsw_module_entity_entity = bsw_module_entity_entity_value

        # Parse td_event_bsw_behavior_type
        child = ARObject._find_child_element(element, "TD-EVENT-BSW-BEHAVIOR-TYPE")
        if child is not None:
            td_event_bsw_behavior_type_value = child.text
            obj.td_event_bsw_behavior_type = td_event_bsw_behavior_type_value

        return obj



class TDEventBswInternalBehaviorBuilder:
    """Builder for TDEventBswInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswInternalBehavior = TDEventBswInternalBehavior()

    def build(self) -> TDEventBswInternalBehavior:
        """Build and return TDEventBswInternalBehavior object.

        Returns:
            TDEventBswInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
