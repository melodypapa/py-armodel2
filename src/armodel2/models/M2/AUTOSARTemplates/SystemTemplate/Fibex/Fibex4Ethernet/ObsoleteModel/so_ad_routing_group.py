"""SoAdRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SoAdRoutingGroup(FibexElement):
    """AUTOSAR SoAdRoutingGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SO-AD-ROUTING-GROUP"


    event_group_ref: Optional[EventGroupControlTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "EVENT-GROUP-REF": lambda obj, elem: setattr(obj, "event_group_ref", EventGroupControlTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SoAdRoutingGroup."""
        super().__init__()
        self.event_group_ref: Optional[EventGroupControlTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize SoAdRoutingGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SoAdRoutingGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_group_ref
        if self.event_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_group_ref, "EventGroupControlTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoAdRoutingGroup":
        """Deserialize XML element to SoAdRoutingGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoAdRoutingGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoAdRoutingGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EVENT-GROUP-REF":
                setattr(obj, "event_group_ref", EventGroupControlTypeEnum.deserialize(child))

        return obj



class SoAdRoutingGroupBuilder(FibexElementBuilder):
    """Builder for SoAdRoutingGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SoAdRoutingGroup = SoAdRoutingGroup()


    def with_event_group(self, value: Optional[EventGroupControlTypeEnum]) -> "SoAdRoutingGroupBuilder":
        """Set event_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_group = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "eventGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SoAdRoutingGroup:
        """Build and return the SoAdRoutingGroup instance with validation."""
        self._validate_instance()
        return self._obj