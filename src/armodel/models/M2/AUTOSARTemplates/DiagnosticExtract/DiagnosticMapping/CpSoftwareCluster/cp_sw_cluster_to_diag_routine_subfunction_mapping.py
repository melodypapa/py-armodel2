"""CpSwClusterToDiagRoutineSubfunctionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 274)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterToDiagRoutineSubfunctionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cp_software_cluster: Optional[CpSoftwareCluster]
    routine: Optional[DiagnosticRoutine]
    def __init__(self) -> None:
        """Initialize CpSwClusterToDiagRoutineSubfunctionMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.routine: Optional[DiagnosticRoutine] = None
    def serialize(self) -> ET.Element:
        """Serialize CpSwClusterToDiagRoutineSubfunctionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSwClusterToDiagRoutineSubfunctionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cp_software_cluster
        if self.cp_software_cluster is not None:
            serialized = ARObject._serialize_item(self.cp_software_cluster, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CP-SOFTWARE-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routine
        if self.routine is not None:
            serialized = ARObject._serialize_item(self.routine, "DiagnosticRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROUTINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterToDiagRoutineSubfunctionMapping":
        """Deserialize XML element to CpSwClusterToDiagRoutineSubfunctionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSwClusterToDiagRoutineSubfunctionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSwClusterToDiagRoutineSubfunctionMapping, cls).deserialize(element)

        # Parse cp_software_cluster
        child = ARObject._find_child_element(element, "CP-SOFTWARE-CLUSTER")
        if child is not None:
            cp_software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.cp_software_cluster = cp_software_cluster_value

        # Parse routine
        child = ARObject._find_child_element(element, "ROUTINE")
        if child is not None:
            routine_value = ARObject._deserialize_by_tag(child, "DiagnosticRoutine")
            obj.routine = routine_value

        return obj



class CpSwClusterToDiagRoutineSubfunctionMappingBuilder:
    """Builder for CpSwClusterToDiagRoutineSubfunctionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterToDiagRoutineSubfunctionMapping = CpSwClusterToDiagRoutineSubfunctionMapping()

    def build(self) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """Build and return CpSwClusterToDiagRoutineSubfunctionMapping object.

        Returns:
            CpSwClusterToDiagRoutineSubfunctionMapping instance
        """
        # TODO: Add validation
        return self._obj
