"""DiagnosticReadDataByPeriodicIDClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate import (
    DiagnosticPeriodicRate,
)


class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByPeriodicIDClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_periodic_did: Optional[PositiveInteger]
    periodic_rates: list[DiagnosticPeriodicRate]
    scheduler_max: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicIDClass."""
        super().__init__()
        self.max_periodic_did: Optional[PositiveInteger] = None
        self.periodic_rates: list[DiagnosticPeriodicRate] = []
        self.scheduler_max: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadDataByPeriodicIDClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadDataByPeriodicIDClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_periodic_did
        if self.max_periodic_did is not None:
            serialized = ARObject._serialize_item(self.max_periodic_did, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-PERIODIC-DID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize periodic_rates (list to container "PERIODIC-RATES")
        if self.periodic_rates:
            wrapper = ET.Element("PERIODIC-RATES")
            for item in self.periodic_rates:
                serialized = ARObject._serialize_item(item, "DiagnosticPeriodicRate")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_max
        if self.scheduler_max is not None:
            serialized = ARObject._serialize_item(self.scheduler_max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCHEDULER-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByPeriodicIDClass":
        """Deserialize XML element to DiagnosticReadDataByPeriodicIDClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByPeriodicIDClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByPeriodicIDClass, cls).deserialize(element)

        # Parse max_periodic_did
        child = ARObject._find_child_element(element, "MAX-PERIODIC-DID")
        if child is not None:
            max_periodic_did_value = child.text
            obj.max_periodic_did = max_periodic_did_value

        # Parse periodic_rates (list from container "PERIODIC-RATES")
        obj.periodic_rates = []
        container = ARObject._find_child_element(element, "PERIODIC-RATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.periodic_rates.append(child_value)

        # Parse scheduler_max
        child = ARObject._find_child_element(element, "SCHEDULER-MAX")
        if child is not None:
            scheduler_max_value = child.text
            obj.scheduler_max = scheduler_max_value

        return obj



class DiagnosticReadDataByPeriodicIDClassBuilder:
    """Builder for DiagnosticReadDataByPeriodicIDClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicIDClass = DiagnosticReadDataByPeriodicIDClass()

    def build(self) -> DiagnosticReadDataByPeriodicIDClass:
        """Build and return DiagnosticReadDataByPeriodicIDClass object.

        Returns:
            DiagnosticReadDataByPeriodicIDClass instance
        """
        # TODO: Add validation
        return self._obj
