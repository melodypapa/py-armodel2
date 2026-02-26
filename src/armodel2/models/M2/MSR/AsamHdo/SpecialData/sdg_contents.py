"""SdgContents AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
        Sdg,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SdgContents(ARObject):
    """AUTOSAR SdgContents."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sd: Optional[Sd]
    sdf: Optional[Sdf]
    sdg: Optional[Sdg]
    sdx_ref: Optional[ARRef]
    sdxf_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx_ref: Optional[ARRef] = None
        self.sdxf_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgContents to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgContents, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sd
        if self.sd is not None:
            serialized = SerializationHelper.serialize_item(self.sd, "Sd")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdf
        if self.sdf is not None:
            serialized = SerializationHelper.serialize_item(self.sdf, "Sdf")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg
        if self.sdg is not None:
            serialized = SerializationHelper.serialize_item(self.sdg, "Sdg")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdx_ref
        if self.sdx_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdx_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDX-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdxf_ref
        if self.sdxf_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdxf_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDXF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgContents":
        """Deserialize XML element to SdgContents object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgContents object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgContents, cls).deserialize(element)

        # Parse sd
        child = SerializationHelper.find_child_element(element, "SD")
        if child is not None:
            sd_value = SerializationHelper.deserialize_by_tag(child, "Sd")
            obj.sd = sd_value

        # Parse sdf
        child = SerializationHelper.find_child_element(element, "SDF")
        if child is not None:
            sdf_value = SerializationHelper.deserialize_by_tag(child, "Sdf")
            obj.sdf = sdf_value

        # Parse sdg
        child = SerializationHelper.find_child_element(element, "SDG")
        if child is not None:
            sdg_value = SerializationHelper.deserialize_by_tag(child, "Sdg")
            obj.sdg = sdg_value

        # Parse sdx_ref
        child = SerializationHelper.find_child_element(element, "SDX-REF")
        if child is not None:
            sdx_ref_value = ARRef.deserialize(child)
            obj.sdx_ref = sdx_ref_value

        # Parse sdxf_ref
        child = SerializationHelper.find_child_element(element, "SDXF-REF")
        if child is not None:
            sdxf_ref_value = ARRef.deserialize(child)
            obj.sdxf_ref = sdxf_ref_value

        return obj



class SdgContentsBuilder(BuilderBase):
    """Builder for SdgContents with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgContents = SdgContents()


    def with_sd(self, value: Optional[Sd]) -> "SdgContentsBuilder":
        """Set sd attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd = value
        return self

    def with_sdf(self, value: Optional[Sdf]) -> "SdgContentsBuilder":
        """Set sdf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdf = value
        return self

    def with_sdg(self, value: Optional[Sdg]) -> "SdgContentsBuilder":
        """Set sdg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdg = value
        return self

    def with_sdx(self, value: Optional[Referrable]) -> "SdgContentsBuilder":
        """Set sdx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdx = value
        return self

    def with_sdxf(self, value: Optional[Referrable]) -> "SdgContentsBuilder":
        """Set sdxf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdxf = value
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


    def build(self) -> SdgContents:
        """Build and return the SdgContents instance with validation."""
        self._validate_instance()
        pass
        return self._obj