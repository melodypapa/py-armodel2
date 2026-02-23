"""DocumentViewSelectable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ViewTokens,
)


class DocumentViewSelectable(ARObject, ABC):
    """AUTOSAR DocumentViewSelectable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    si: NameTokens
    view: Optional[ViewTokens]
    def __init__(self) -> None:
        """Initialize DocumentViewSelectable."""
        super().__init__()
        self.si: NameTokens = None
        self.view: Optional[ViewTokens] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentViewSelectable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentViewSelectable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize si
        if self.si is not None:
            serialized = SerializationHelper.serialize_item(self.si, "NameTokens")
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

        # Serialize view
        if self.view is not None:
            serialized = SerializationHelper.serialize_item(self.view, "ViewTokens")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VIEW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentViewSelectable":
        """Deserialize XML element to DocumentViewSelectable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentViewSelectable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentViewSelectable, cls).deserialize(element)

        # Parse si
        child = SerializationHelper.find_child_element(element, "SI")
        if child is not None:
            si_value = child.text
            obj.si = si_value

        # Parse view
        child = SerializationHelper.find_child_element(element, "VIEW")
        if child is not None:
            view_value = child.text
            obj.view = view_value

        return obj



class DocumentViewSelectableBuilder(BuilderBase, ABC):
    """Builder for DocumentViewSelectable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DocumentViewSelectable = DocumentViewSelectable()


    def with_si(self, value: NameTokens) -> "DocumentViewSelectableBuilder":
        """Set si attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.si = value
        return self

    def with_view(self, value: Optional[ViewTokens]) -> "DocumentViewSelectableBuilder":
        """Set view attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.view = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    @abstractmethod
    def build(self) -> DocumentViewSelectable:
        """Build and return the DocumentViewSelectable instance (abstract)."""
        raise NotImplementedError