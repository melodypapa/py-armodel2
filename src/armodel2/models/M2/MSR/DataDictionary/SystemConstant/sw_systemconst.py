"""SwSystemconst AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 448)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2068)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_SystemConstant.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwSystemconst(ARElement):
    """AUTOSAR SwSystemconst."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize SwSystemconst."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SwSystemconst to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwSystemconst, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconst":
        """Deserialize XML element to SwSystemconst object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwSystemconst object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwSystemconst, cls).deserialize(element)

        # Parse sw_data_def
        child = SerializationHelper.find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class SwSystemconstBuilder(ARElementBuilder):
    """Builder for SwSystemconst with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwSystemconst = SwSystemconst()


    def with_sw_data_def(self, value: Optional[SwDataDefProps]) -> "SwSystemconstBuilder":
        """Set sw_data_def attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data_def = value
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


    def build(self) -> SwSystemconst:
        """Build and return the SwSystemconst instance with validation."""
        self._validate_instance()
        pass
        return self._obj