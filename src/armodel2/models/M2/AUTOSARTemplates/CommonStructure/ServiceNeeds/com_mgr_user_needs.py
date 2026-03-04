"""ComMgrUserNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 711)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    MaxCommModeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ComMgrUserNeeds(ServiceNeeds):
    """AUTOSAR ComMgrUserNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COM-MGR-USER-NEEDS"


    max_comm_mode_enum: Optional[MaxCommModeEnum]
    _DESERIALIZE_DISPATCH = {
        "MAX-COMM-MODE-ENUM": lambda obj, elem: setattr(obj, "max_comm_mode_enum", MaxCommModeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ComMgrUserNeeds."""
        super().__init__()
        self.max_comm_mode_enum: Optional[MaxCommModeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ComMgrUserNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ComMgrUserNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_comm_mode_enum
        if self.max_comm_mode_enum is not None:
            serialized = SerializationHelper.serialize_item(self.max_comm_mode_enum, "MaxCommModeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-COMM-MODE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComMgrUserNeeds":
        """Deserialize XML element to ComMgrUserNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComMgrUserNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComMgrUserNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX-COMM-MODE-ENUM":
                setattr(obj, "max_comm_mode_enum", MaxCommModeEnum.deserialize(child))

        return obj



class ComMgrUserNeedsBuilder(ServiceNeedsBuilder):
    """Builder for ComMgrUserNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ComMgrUserNeeds = ComMgrUserNeeds()


    def with_max_comm_mode_enum(self, value: Optional[MaxCommModeEnum]) -> "ComMgrUserNeedsBuilder":
        """Set max_comm_mode_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_comm_mode_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maxCommModeEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ComMgrUserNeeds:
        """Build and return the ComMgrUserNeeds instance with validation."""
        self._validate_instance()
        return self._obj