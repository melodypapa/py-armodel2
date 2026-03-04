"""UserDefinedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 346)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import IPduBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class UserDefinedIPdu(IPdu):
    """AUTOSAR UserDefinedIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "USER-DEFINED-I-PDU"


    cdd_type: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "CDD-TYPE": lambda obj, elem: setattr(obj, "cdd_type", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize UserDefinedIPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize UserDefinedIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cdd_type
        if self.cdd_type is not None:
            serialized = SerializationHelper.serialize_item(self.cdd_type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CDD-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedIPdu":
        """Deserialize XML element to UserDefinedIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UserDefinedIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CDD-TYPE":
                setattr(obj, "cdd_type", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class UserDefinedIPduBuilder(IPduBuilder):
    """Builder for UserDefinedIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UserDefinedIPdu = UserDefinedIPdu()


    def with_cdd_type(self, value: Optional[String]) -> "UserDefinedIPduBuilder":
        """Set cdd_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cdd_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cddType",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UserDefinedIPdu:
        """Build and return the UserDefinedIPdu instance with validation."""
        self._validate_instance()
        return self._obj