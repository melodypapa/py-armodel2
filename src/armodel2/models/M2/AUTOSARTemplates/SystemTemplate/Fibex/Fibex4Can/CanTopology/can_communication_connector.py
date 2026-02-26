"""CanCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 74)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import (
    AbstractCanCommunicationConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import AbstractCanCommunicationConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    PositiveUnlimitedInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """AUTOSAR CanCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pnc_wakeup_can: Optional[PositiveInteger]
    pnc_wakeup: Optional[PositiveUnlimitedInteger]
    pnc_wakeup_dlc: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanCommunicationConnector."""
        super().__init__()
        self.pnc_wakeup_can: Optional[PositiveInteger] = None
        self.pnc_wakeup: Optional[PositiveUnlimitedInteger] = None
        self.pnc_wakeup_dlc: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CanCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pnc_wakeup_can
        if self.pnc_wakeup_can is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup_can, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP-CAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_wakeup
        if self.pnc_wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_wakeup_dlc
        if self.pnc_wakeup_dlc is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup_dlc, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP-DLC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanCommunicationConnector":
        """Deserialize XML element to CanCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanCommunicationConnector, cls).deserialize(element)

        # Parse pnc_wakeup_can
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP-CAN")
        if child is not None:
            pnc_wakeup_can_value = child.text
            obj.pnc_wakeup_can = pnc_wakeup_can_value

        # Parse pnc_wakeup
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse pnc_wakeup_dlc
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP-DLC")
        if child is not None:
            pnc_wakeup_dlc_value = child.text
            obj.pnc_wakeup_dlc = pnc_wakeup_dlc_value

        return obj



class CanCommunicationConnectorBuilder(AbstractCanCommunicationConnectorBuilder):
    """Builder for CanCommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanCommunicationConnector = CanCommunicationConnector()


    def with_pnc_wakeup_can(self, value: Optional[PositiveInteger]) -> "CanCommunicationConnectorBuilder":
        """Set pnc_wakeup_can attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_wakeup_can = value
        return self

    def with_pnc_wakeup(self, value: Optional[PositiveUnlimitedInteger]) -> "CanCommunicationConnectorBuilder":
        """Set pnc_wakeup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_wakeup = value
        return self

    def with_pnc_wakeup_dlc(self, value: Optional[PositiveInteger]) -> "CanCommunicationConnectorBuilder":
        """Set pnc_wakeup_dlc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_wakeup_dlc = value
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


    def build(self) -> CanCommunicationConnector:
        """Build and return the CanCommunicationConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj