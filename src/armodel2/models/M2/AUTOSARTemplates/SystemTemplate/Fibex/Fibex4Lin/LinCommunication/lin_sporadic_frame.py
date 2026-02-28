"""LinSporadicFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import LinFrameBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinSporadicFrame(LinFrame):
    """AUTOSAR LinSporadicFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-SPORADIC-FRAME"


    substituted_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SUBSTITUTEDS": lambda obj, elem: obj.substituted_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize LinSporadicFrame."""
        super().__init__()
        self.substituted_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize LinSporadicFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinSporadicFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize substituted_refs (list to container "SUBSTITUTED-REFS")
        if self.substituted_refs:
            wrapper = ET.Element("SUBSTITUTED-REFS")
            for item in self.substituted_refs:
                serialized = SerializationHelper.serialize_item(item, "LinUnconditionalFrame")
                if serialized is not None:
                    child_elem = ET.Element("SUBSTITUTED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSporadicFrame":
        """Deserialize XML element to LinSporadicFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSporadicFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinSporadicFrame, cls).deserialize(element)

        # Parse substituted_refs (list from container "SUBSTITUTED-REFS")
        obj.substituted_refs = []
        container = SerializationHelper.find_child_element(element, "SUBSTITUTED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.substituted_refs.append(child_value)

        return obj



class LinSporadicFrameBuilder(LinFrameBuilder):
    """Builder for LinSporadicFrame with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinSporadicFrame = LinSporadicFrame()


    def with_substituteds(self, items: list[LinUnconditionalFrame]) -> "LinSporadicFrameBuilder":
        """Set substituteds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.substituteds = list(items) if items else []
        return self


    def add_substituted(self, item: LinUnconditionalFrame) -> "LinSporadicFrameBuilder":
        """Add a single item to substituteds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.substituteds.append(item)
        return self

    def clear_substituteds(self) -> "LinSporadicFrameBuilder":
        """Clear all items from substituteds list.

        Returns:
            self for method chaining
        """
        self._obj.substituteds = []
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


    def build(self) -> LinSporadicFrame:
        """Build and return the LinSporadicFrame instance with validation."""
        self._validate_instance()
        pass
        return self._obj