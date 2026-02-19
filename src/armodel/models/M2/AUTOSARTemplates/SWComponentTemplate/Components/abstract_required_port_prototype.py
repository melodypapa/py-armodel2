"""AbstractRequiredPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from abc import ABC, abstractmethod


class AbstractRequiredPortPrototype(PortPrototype, ABC):
    """AUTOSAR AbstractRequiredPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    required_coms: list[RPortComSpec]
    def __init__(self) -> None:
        """Initialize AbstractRequiredPortPrototype."""
        super().__init__()
        self.required_coms: list[RPortComSpec] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractRequiredPortPrototype":
        """Deserialize XML element to AbstractRequiredPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractRequiredPortPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse required_coms (list)
        obj.required_coms = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-COMS"):
            required_coms_value = ARObject._deserialize_by_tag(child, "RPortComSpec")
            obj.required_coms.append(required_coms_value)

        return obj



class AbstractRequiredPortPrototypeBuilder:
    """Builder for AbstractRequiredPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRequiredPortPrototype = AbstractRequiredPortPrototype()

    def build(self) -> AbstractRequiredPortPrototype:
        """Build and return AbstractRequiredPortPrototype object.

        Returns:
            AbstractRequiredPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
