"""NmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class NmCluster(Identifiable, ABC):
    """AUTOSAR NmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_cluster_ref: Optional[ARRef]
    nm_channel: Optional[Boolean]
    nm_node: Optional[Boolean]
    nm_node_id_enabled: Optional[Boolean]
    nm_pnc: Optional[Boolean]
    nm_repeat_msg_ind_enabled: Optional[Boolean]
    nm: Optional[Boolean]
    pnc_cluster: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NmCluster."""
        super().__init__()
        self.communication_cluster_ref: Optional[ARRef] = None
        self.nm_channel: Optional[Boolean] = None
        self.nm_node: Optional[Boolean] = None
        self.nm_node_id_enabled: Optional[Boolean] = None
        self.nm_pnc: Optional[Boolean] = None
        self.nm_repeat_msg_ind_enabled: Optional[Boolean] = None
        self.nm: Optional[Boolean] = None
        self.pnc_cluster: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize NmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_cluster_ref
        if self.communication_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_cluster_ref, "CommunicationCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_channel
        if self.nm_channel is not None:
            serialized = SerializationHelper.serialize_item(self.nm_channel, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node
        if self.nm_node is not None:
            serialized = SerializationHelper.serialize_item(self.nm_node, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_node_id_enabled
        if self.nm_node_id_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.nm_node_id_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NODE-ID-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_pnc
        if self.nm_pnc is not None:
            serialized = SerializationHelper.serialize_item(self.nm_pnc, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-PNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repeat_msg_ind_enabled
        if self.nm_repeat_msg_ind_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.nm_repeat_msg_ind_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPEAT-MSG-IND-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm
        if self.nm is not None:
            serialized = SerializationHelper.serialize_item(self.nm, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_cluster
        if self.pnc_cluster is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_cluster, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCluster":
        """Deserialize XML element to NmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmCluster, cls).deserialize(element)

        # Parse communication_cluster_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CLUSTER-REF")
        if child is not None:
            communication_cluster_ref_value = ARRef.deserialize(child)
            obj.communication_cluster_ref = communication_cluster_ref_value

        # Parse nm_channel
        child = SerializationHelper.find_child_element(element, "NM-CHANNEL")
        if child is not None:
            nm_channel_value = child.text
            obj.nm_channel = nm_channel_value

        # Parse nm_node
        child = SerializationHelper.find_child_element(element, "NM-NODE")
        if child is not None:
            nm_node_value = child.text
            obj.nm_node = nm_node_value

        # Parse nm_node_id_enabled
        child = SerializationHelper.find_child_element(element, "NM-NODE-ID-ENABLED")
        if child is not None:
            nm_node_id_enabled_value = child.text
            obj.nm_node_id_enabled = nm_node_id_enabled_value

        # Parse nm_pnc
        child = SerializationHelper.find_child_element(element, "NM-PNC")
        if child is not None:
            nm_pnc_value = child.text
            obj.nm_pnc = nm_pnc_value

        # Parse nm_repeat_msg_ind_enabled
        child = SerializationHelper.find_child_element(element, "NM-REPEAT-MSG-IND-ENABLED")
        if child is not None:
            nm_repeat_msg_ind_enabled_value = child.text
            obj.nm_repeat_msg_ind_enabled = nm_repeat_msg_ind_enabled_value

        # Parse nm
        child = SerializationHelper.find_child_element(element, "NM")
        if child is not None:
            nm_value = child.text
            obj.nm = nm_value

        # Parse pnc_cluster
        child = SerializationHelper.find_child_element(element, "PNC-CLUSTER")
        if child is not None:
            pnc_cluster_value = child.text
            obj.pnc_cluster = pnc_cluster_value

        return obj



class NmClusterBuilder(IdentifiableBuilder):
    """Builder for NmCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NmCluster = NmCluster()


    def with_communication_cluster(self, value: Optional[CommunicationCluster]) -> "NmClusterBuilder":
        """Set communication_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication_cluster = value
        return self

    def with_nm_channel(self, value: Optional[Boolean]) -> "NmClusterBuilder":
        """Set nm_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_channel = value
        return self

    def with_nm_node(self, value: Optional[Boolean]) -> "NmClusterBuilder":
        """Set nm_node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_node = value
        return self

    def with_nm_node_id_enabled(self, value: Optional[Boolean]) -> "NmClusterBuilder":
        """Set nm_node_id_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_node_id_enabled = value
        return self

    def with_nm_pnc(self, value: Optional[Boolean]) -> "NmClusterBuilder":
        """Set nm_pnc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_pnc = value
        return self

    def with_nm_repeat_msg_ind_enabled(self, value: Optional[Boolean]) -> "NmClusterBuilder":
        """Set nm_repeat_msg_ind_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_repeat_msg_ind_enabled = value
        return self

    def with_nm(self, value: Optional[Boolean]) -> "NmClusterBuilder":
        """Set nm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm = value
        return self

    def with_pnc_cluster(self, value: Optional[PositiveInteger]) -> "NmClusterBuilder":
        """Set pnc_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_cluster = value
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
    def build(self) -> NmCluster:
        """Build and return the NmCluster instance (abstract)."""
        raise NotImplementedError