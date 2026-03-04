"""EcuPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcuPartition(Identifiable):
    """AUTOSAR EcuPartition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECU-PARTITION"


    exec_in_user: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "EXEC-IN-USER": lambda obj, elem: setattr(obj, "exec_in_user", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize EcuPartition."""
        super().__init__()
        self.exec_in_user: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcuPartition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuPartition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize exec_in_user
        if self.exec_in_user is not None:
            serialized = SerializationHelper.serialize_item(self.exec_in_user, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXEC-IN-USER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuPartition":
        """Deserialize XML element to EcuPartition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuPartition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuPartition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXEC-IN-USER":
                setattr(obj, "exec_in_user", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class EcuPartitionBuilder(IdentifiableBuilder):
    """Builder for EcuPartition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcuPartition = EcuPartition()


    def with_exec_in_user(self, value: Optional[Boolean]) -> "EcuPartitionBuilder":
        """Set exec_in_user attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.exec_in_user = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "execInUser",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcuPartition:
        """Build and return the EcuPartition instance with validation."""
        self._validate_instance()
        return self._obj