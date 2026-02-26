"""MsrQueryP2 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 456)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class MsrQueryP2(ARObject):
    """AUTOSAR MsrQueryP2."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize MsrQueryP2."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[DocumentationBlock] = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryP2 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryP2, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query_props
        if self.msr_query_props is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_props, "MsrQueryProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_result (atp_mixed - append children directly)
        if self.msr_query_result is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_result, "DocumentationBlock")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP2":
        """Deserialize XML element to MsrQueryP2 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryP2 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryP2, cls).deserialize(element)

        # Parse msr_query_props
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-RESULT")
        if child is not None:
            msr_query_result_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.msr_query_result = msr_query_result_value

        return obj



class MsrQueryP2Builder(BuilderBase):
    """Builder for MsrQueryP2 with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MsrQueryP2 = MsrQueryP2()


    def with_msr_query_props(self, value: MsrQueryProps) -> "MsrQueryP2Builder":
        """Set msr_query_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_props = value
        return self

    def with_msr_query_result(self, value: Optional[DocumentationBlock]) -> "MsrQueryP2Builder":
        """Set msr_query_result attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_result = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> MsrQueryP2:
        """Build and return the MsrQueryP2 instance with validation."""
        self._validate_instance()
        pass
        return self._obj