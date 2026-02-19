"""DltApplication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 8)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)


class DltApplication(Identifiable):
    """AUTOSAR DltApplication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application: Optional[String]
    application_id: Optional[String]
    contexts: list[DltContext]
    def __init__(self) -> None:
        """Initialize DltApplication."""
        super().__init__()
        self.application: Optional[String] = None
        self.application_id: Optional[String] = None
        self.contexts: list[DltContext] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltApplication":
        """Deserialize XML element to DltApplication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltApplication object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse application
        child = ARObject._find_child_element(element, "APPLICATION")
        if child is not None:
            application_value = child.text
            obj.application = application_value

        # Parse application_id
        child = ARObject._find_child_element(element, "APPLICATION-ID")
        if child is not None:
            application_id_value = child.text
            obj.application_id = application_id_value

        # Parse contexts (list)
        obj.contexts = []
        for child in ARObject._find_all_child_elements(element, "CONTEXTS"):
            contexts_value = ARObject._deserialize_by_tag(child, "DltContext")
            obj.contexts.append(contexts_value)

        return obj



class DltApplicationBuilder:
    """Builder for DltApplication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltApplication = DltApplication()

    def build(self) -> DltApplication:
        """Build and return DltApplication object.

        Returns:
            DltApplication instance
        """
        # TODO: Add validation
        return self._obj
