"""MacSecParticipantSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_kay_participant import (
    MacSecKayParticipant,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class MacSecParticipantSet(ARElement):
    """AUTOSAR MacSecParticipantSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ethernet_cluster_ref: Optional[ARRef]
    mka_participants: list[MacSecKayParticipant]
    def __init__(self) -> None:
        """Initialize MacSecParticipantSet."""
        super().__init__()
        self.ethernet_cluster_ref: Optional[ARRef] = None
        self.mka_participants: list[MacSecKayParticipant] = []

    def serialize(self) -> ET.Element:
        """Serialize MacSecParticipantSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecParticipantSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ethernet_cluster_ref
        if self.ethernet_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ethernet_cluster_ref, "EthernetCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETHERNET-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mka_participants (list to container "MKA-PARTICIPANTS")
        if self.mka_participants:
            wrapper = ET.Element("MKA-PARTICIPANTS")
            for item in self.mka_participants:
                serialized = SerializationHelper.serialize_item(item, "MacSecKayParticipant")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecParticipantSet":
        """Deserialize XML element to MacSecParticipantSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecParticipantSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecParticipantSet, cls).deserialize(element)

        # Parse ethernet_cluster_ref
        child = SerializationHelper.find_child_element(element, "ETHERNET-CLUSTER-REF")
        if child is not None:
            ethernet_cluster_ref_value = ARRef.deserialize(child)
            obj.ethernet_cluster_ref = ethernet_cluster_ref_value

        # Parse mka_participants (list from container "MKA-PARTICIPANTS")
        obj.mka_participants = []
        container = SerializationHelper.find_child_element(element, "MKA-PARTICIPANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mka_participants.append(child_value)

        return obj



class MacSecParticipantSetBuilder(ARElementBuilder):
    """Builder for MacSecParticipantSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecParticipantSet = MacSecParticipantSet()


    def with_ethernet_cluster(self, value: Optional[EthernetCluster]) -> "MacSecParticipantSetBuilder":
        """Set ethernet_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ethernet_cluster = value
        return self

    def with_mka_participants(self, items: list[MacSecKayParticipant]) -> "MacSecParticipantSetBuilder":
        """Set mka_participants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mka_participants = list(items) if items else []
        return self


    def add_mka_participant(self, item: MacSecKayParticipant) -> "MacSecParticipantSetBuilder":
        """Add a single item to mka_participants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mka_participants.append(item)
        return self

    def clear_mka_participants(self) -> "MacSecParticipantSetBuilder":
        """Clear all items from mka_participants list.

        Returns:
            self for method chaining
        """
        self._obj.mka_participants = []
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


    def build(self) -> MacSecParticipantSet:
        """Build and return the MacSecParticipantSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj