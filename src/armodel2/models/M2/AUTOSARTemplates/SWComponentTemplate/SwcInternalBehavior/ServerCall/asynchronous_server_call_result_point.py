"""AsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 581)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import AbstractAccessPointBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """AUTOSAR AsynchronousServerCallResultPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"


    asynchronous_server_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "ASYNCHRONOUS-SERVER-REF": lambda obj, elem: setattr(obj, "asynchronous_server_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize AsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous_server_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize AsynchronousServerCallResultPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AsynchronousServerCallResultPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize asynchronous_server_ref
        if self.asynchronous_server_ref is not None:
            serialized = SerializationHelper.serialize_item(self.asynchronous_server_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASYNCHRONOUS-SERVER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AsynchronousServerCallResultPoint":
        """Deserialize XML element to AsynchronousServerCallResultPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AsynchronousServerCallResultPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AsynchronousServerCallResultPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASYNCHRONOUS-SERVER-REF":
                setattr(obj, "asynchronous_server_ref", ARRef.deserialize(child))

        return obj



class AsynchronousServerCallResultPointBuilder(AbstractAccessPointBuilder):
    """Builder for AsynchronousServerCallResultPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AsynchronousServerCallResultPoint = AsynchronousServerCallResultPoint()


    def with_asynchronous_server(self, value: Optional[Any]) -> "AsynchronousServerCallResultPointBuilder":
        """Set asynchronous_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'asynchronous_server' is required and cannot be None")
        self._obj.asynchronous_server = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "asynchronousServer",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AsynchronousServerCallResultPoint:
        """Build and return the AsynchronousServerCallResultPoint instance with validation."""
        self._validate_instance()
        return self._obj