"""ClientServerOperationComProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import CpSoftwareClusterCommunicationResourcePropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR ClientServerOperationComProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-OPERATION-COM-PROPS"


    queue_length: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "QUEUE-LENGTH": lambda obj, elem: setattr(obj, "queue_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ClientServerOperationComProps."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperationComProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerOperationComProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize queue_length
        if self.queue_length is not None:
            serialized = SerializationHelper.serialize_item(self.queue_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("QUEUE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationComProps":
        """Deserialize XML element to ClientServerOperationComProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperationComProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperationComProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "QUEUE-LENGTH":
                setattr(obj, "queue_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ClientServerOperationComPropsBuilder(CpSoftwareClusterCommunicationResourcePropsBuilder):
    """Builder for ClientServerOperationComProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerOperationComProps = ClientServerOperationComProps()


    def with_queue_length(self, value: Optional[PositiveInteger]) -> "ClientServerOperationComPropsBuilder":
        """Set queue_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.queue_length = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "queueLength",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ClientServerOperationComProps:
        """Build and return the ClientServerOperationComProps instance with validation."""
        self._validate_instance()
        return self._obj