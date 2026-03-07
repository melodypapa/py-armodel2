"""DdsCpTopic AUTOSAR element.

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
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_partition import (
    DdsCpPartition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpTopic(Identifiable):
    """AUTOSAR DdsCpTopic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-TOPIC"


    dds_partition_ref: Optional[ARRef]
    topic_name: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "DDS-PARTITION-REF": lambda obj, elem: setattr(obj, "dds_partition_ref", ARRef.deserialize(elem)),
        "TOPIC-NAME": lambda obj, elem: setattr(obj, "topic_name", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize DdsCpTopic."""
        super().__init__()
        self.dds_partition_ref: Optional[ARRef] = None
        self.topic_name: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpTopic to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpTopic, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_partition_ref
        if self.dds_partition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_partition_ref, "DdsCpPartition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-PARTITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic_name
        if self.topic_name is not None:
            serialized = SerializationHelper.serialize_item(self.topic_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOPIC-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpTopic":
        """Deserialize XML element to DdsCpTopic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpTopic object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpTopic, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DDS-PARTITION-REF":
                setattr(obj, "dds_partition_ref", ARRef.deserialize(child))
            elif tag == "TOPIC-NAME":
                setattr(obj, "topic_name", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class DdsCpTopicBuilder(IdentifiableBuilder):
    """Builder for DdsCpTopic with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpTopic = DdsCpTopic()


    def with_dds_partition(self, value: Optional[DdsCpPartition]) -> "DdsCpTopicBuilder":
        """Set dds_partition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'dds_partition' is required and cannot be None")
        self._obj.dds_partition = value
        return self

    def with_topic_name(self, value: Optional[String]) -> "DdsCpTopicBuilder":
        """Set topic_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'topic_name' is required and cannot be None")
        self._obj.topic_name = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ddsPartition",
        "topicName",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsCpTopic:
        """Build and return the DdsCpTopic instance with validation."""
        self._validate_instance()
        return self._obj