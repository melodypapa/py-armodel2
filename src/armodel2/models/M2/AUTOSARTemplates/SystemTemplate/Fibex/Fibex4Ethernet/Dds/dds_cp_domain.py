"""DdsCpDomain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 526)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_partition import (
    DdsCpPartition,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpDomain(Identifiable):
    """AUTOSAR DdsCpDomain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-DOMAIN"


    dds_partitions: list[DdsCpPartition]
    dds_topics: list[DdsCpTopic]
    domain_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "DDS-PARTITIONS": lambda obj, elem: obj.dds_partitions.append(SerializationHelper.deserialize_by_tag(elem, "DdsCpPartition")),
        "DDS-TOPICS": lambda obj, elem: obj.dds_topics.append(SerializationHelper.deserialize_by_tag(elem, "DdsCpTopic")),
        "DOMAIN-ID": lambda obj, elem: setattr(obj, "domain_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DdsCpDomain."""
        super().__init__()
        self.dds_partitions: list[DdsCpPartition] = []
        self.dds_topics: list[DdsCpTopic] = []
        self.domain_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpDomain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpDomain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_partitions (list to container "DDS-PARTITIONS")
        if self.dds_partitions:
            wrapper = ET.Element("DDS-PARTITIONS")
            for item in self.dds_partitions:
                serialized = SerializationHelper.serialize_item(item, "DdsCpPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dds_topics (list to container "DDS-TOPICS")
        if self.dds_topics:
            wrapper = ET.Element("DDS-TOPICS")
            for item in self.dds_topics:
                serialized = SerializationHelper.serialize_item(item, "DdsCpTopic")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize domain_id
        if self.domain_id is not None:
            serialized = SerializationHelper.serialize_item(self.domain_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOMAIN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpDomain":
        """Deserialize XML element to DdsCpDomain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpDomain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpDomain, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DDS-PARTITIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dds_partitions.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpPartition"))
            elif tag == "DDS-TOPICS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dds_topics.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpTopic"))
            elif tag == "DOMAIN-ID":
                setattr(obj, "domain_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DdsCpDomainBuilder(IdentifiableBuilder):
    """Builder for DdsCpDomain with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpDomain = DdsCpDomain()


    def with_dds_partitions(self, items: list[DdsCpPartition]) -> "DdsCpDomainBuilder":
        """Set dds_partitions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dds_partitions = list(items) if items else []
        return self

    def with_dds_topics(self, items: list[DdsCpTopic]) -> "DdsCpDomainBuilder":
        """Set dds_topics list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dds_topics = list(items) if items else []
        return self

    def with_domain_id(self, value: Optional[PositiveInteger]) -> "DdsCpDomainBuilder":
        """Set domain_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'domain_id' is required and cannot be None")
        self._obj.domain_id = value
        return self


    def add_dds_partition(self, item: DdsCpPartition) -> "DdsCpDomainBuilder":
        """Add a single item to dds_partitions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dds_partitions.append(item)
        return self

    def clear_dds_partitions(self) -> "DdsCpDomainBuilder":
        """Clear all items from dds_partitions list.

        Returns:
            self for method chaining
        """
        self._obj.dds_partitions = []
        return self

    def add_dds_topic(self, item: DdsCpTopic) -> "DdsCpDomainBuilder":
        """Add a single item to dds_topics list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dds_topics.append(item)
        return self

    def clear_dds_topics(self) -> "DdsCpDomainBuilder":
        """Clear all items from dds_topics list.

        Returns:
            self for method chaining
        """
        self._obj.dds_topics = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ddsPartition",
        "ddsTopic",
        "domainId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsCpDomain:
        """Build and return the DdsCpDomain instance with validation."""
        self._validate_instance()
        return self._obj