"""DltEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 8)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_application import (
    DltApplication,
)


class DltEcu(ARElement):
    """AUTOSAR DltEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[DltApplication]
    ecu_id: Optional[String]
    def __init__(self) -> None:
        """Initialize DltEcu."""
        super().__init__()
        self.applications: list[DltApplication] = []
        self.ecu_id: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltEcu":
        """Deserialize XML element to DltEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltEcu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse applications (list)
        obj.applications = []
        for child in ARObject._find_all_child_elements(element, "APPLICATIONS"):
            applications_value = ARObject._deserialize_by_tag(child, "DltApplication")
            obj.applications.append(applications_value)

        # Parse ecu_id
        child = ARObject._find_child_element(element, "ECU-ID")
        if child is not None:
            ecu_id_value = child.text
            obj.ecu_id = ecu_id_value

        return obj



class DltEcuBuilder:
    """Builder for DltEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltEcu = DltEcu()

    def build(self) -> DltEcu:
        """Build and return DltEcu object.

        Returns:
            DltEcu instance
        """
        # TODO: Add validation
        return self._obj
