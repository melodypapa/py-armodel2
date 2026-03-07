"""MsrQueryArg AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MsrQueryArg(ARObject):
    """AUTOSAR MsrQueryArg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MSR-QUERY-ARG"


    arg: String
    si: NameToken
    _DESERIALIZE_DISPATCH = {
        "ARG": lambda obj, elem: setattr(obj, "arg", SerializationHelper.deserialize_by_tag(elem, "String")),
        "SI": lambda obj, elem: setattr(obj, "si", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize MsrQueryArg."""
        super().__init__()
        self.arg: String = None
        self.si: NameToken = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryArg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryArg, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arg
        if self.arg is not None:
            serialized = SerializationHelper.serialize_item(self.arg, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize si
        if self.si is not None:
            serialized = SerializationHelper.serialize_item(self.si, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryArg":
        """Deserialize XML element to MsrQueryArg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryArg object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryArg, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARG":
                setattr(obj, "arg", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "SI":
                setattr(obj, "si", SerializationHelper.deserialize_by_tag(child, "NameToken"))

        return obj



class MsrQueryArgBuilder(BuilderBase):
    """Builder for MsrQueryArg with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MsrQueryArg = MsrQueryArg()


    def with_arg(self, value: String) -> "MsrQueryArgBuilder":
        """Set arg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'arg' is required and cannot be None")
        self._obj.arg = value
        return self

    def with_si(self, value: NameToken) -> "MsrQueryArgBuilder":
        """Set si attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'si' is required and cannot be None")
        self._obj.si = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "arg",
        "si",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "arg", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'arg' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'arg' is None", UserWarning)
        if getattr(self._obj, "si", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'si' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'si' is None", UserWarning)


    def build(self) -> MsrQueryArg:
        """Build and return the MsrQueryArg instance with validation."""
        self._validate_instance()
        return self._obj