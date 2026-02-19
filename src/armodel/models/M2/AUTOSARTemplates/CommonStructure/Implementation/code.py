"""Code AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 130)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class Code(Identifiable):
    """AUTOSAR Code."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    artifacts: list[AutosarEngineeringObject]
    callback_headers: list[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize Code."""
        super().__init__()
        self.artifacts: list[AutosarEngineeringObject] = []
        self.callback_headers: list[ServiceNeeds] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Code":
        """Deserialize XML element to Code object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Code object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse artifacts (list)
        obj.artifacts = []
        for child in ARObject._find_all_child_elements(element, "ARTIFACTS"):
            artifacts_value = ARObject._deserialize_by_tag(child, "AutosarEngineeringObject")
            obj.artifacts.append(artifacts_value)

        # Parse callback_headers (list)
        obj.callback_headers = []
        for child in ARObject._find_all_child_elements(element, "CALLBACK-HEADERS"):
            callback_headers_value = ARObject._deserialize_by_tag(child, "ServiceNeeds")
            obj.callback_headers.append(callback_headers_value)

        return obj



class CodeBuilder:
    """Builder for Code."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Code = Code()

    def build(self) -> Code:
        """Build and return Code object.

        Returns:
            Code instance
        """
        # TODO: Add validation
        return self._obj
