"""CpSwClusterToDiagEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 272)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import DiagnosticMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterToDiagEventMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SW-CLUSTER-TO-DIAG-EVENT-MAPPING"


    cp_software_cluster_ref: Optional[ARRef]
    diagnostic_event_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CP-SOFTWARE-CLUSTER-REF": lambda obj, elem: setattr(obj, "cp_software_cluster_ref", ARRef.deserialize(elem)),
        "DIAGNOSTIC-EVENT-REF": lambda obj, elem: setattr(obj, "diagnostic_event_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CpSwClusterToDiagEventMapping."""
        super().__init__()
        self.cp_software_cluster_ref: Optional[ARRef] = None
        self.diagnostic_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSwClusterToDiagEventMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSwClusterToDiagEventMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cp_software_cluster_ref
        if self.cp_software_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.cp_software_cluster_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CP-SOFTWARE-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_event_ref
        if self.diagnostic_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterToDiagEventMapping":
        """Deserialize XML element to CpSwClusterToDiagEventMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSwClusterToDiagEventMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSwClusterToDiagEventMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CP-SOFTWARE-CLUSTER-REF":
                setattr(obj, "cp_software_cluster_ref", ARRef.deserialize(child))
            elif tag == "DIAGNOSTIC-EVENT-REF":
                setattr(obj, "diagnostic_event_ref", ARRef.deserialize(child))

        return obj



class CpSwClusterToDiagEventMappingBuilder(DiagnosticMappingBuilder):
    """Builder for CpSwClusterToDiagEventMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSwClusterToDiagEventMapping = CpSwClusterToDiagEventMapping()


    def with_cp_software_cluster(self, value: Optional[CpSoftwareCluster]) -> "CpSwClusterToDiagEventMappingBuilder":
        """Set cp_software_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cp_software_cluster = value
        return self

    def with_diagnostic_event(self, value: Optional[DiagnosticEvent]) -> "CpSwClusterToDiagEventMappingBuilder":
        """Set diagnostic_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_event = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cpSoftwareCluster",
        "diagnosticEvent",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CpSwClusterToDiagEventMapping:
        """Build and return the CpSwClusterToDiagEventMapping instance with validation."""
        self._validate_instance()
        return self._obj