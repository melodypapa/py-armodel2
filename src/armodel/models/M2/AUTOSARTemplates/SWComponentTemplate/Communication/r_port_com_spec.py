"""RPortComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 167)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class RPortComSpec(ARObject, ABC):
    """AUTOSAR RPortComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize RPortComSpec."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortComSpec":
        """Deserialize XML element to RPortComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RPortComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class RPortComSpecBuilder:
    """Builder for RPortComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortComSpec = RPortComSpec()

    def build(self) -> RPortComSpec:
        """Build and return RPortComSpec object.

        Returns:
            RPortComSpec instance
        """
        # TODO: Add validation
        return self._obj
