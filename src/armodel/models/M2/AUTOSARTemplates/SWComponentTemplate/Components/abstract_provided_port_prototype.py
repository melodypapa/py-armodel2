"""AbstractProvidedPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from abc import ABC, abstractmethod


class AbstractProvidedPortPrototype(PortPrototype, ABC):
    """AUTOSAR AbstractProvidedPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    provided_coms: list[PPortComSpec]
    def __init__(self) -> None:
        """Initialize AbstractProvidedPortPrototype."""
        super().__init__()
        self.provided_coms: list[PPortComSpec] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractProvidedPortPrototype":
        """Deserialize XML element to AbstractProvidedPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractProvidedPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractProvidedPortPrototype, cls).deserialize(element)

        # Parse provided_coms (list from container "PROVIDED-COMS")
        obj.provided_coms = []
        container = ARObject._find_child_element(element, "PROVIDED-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_coms.append(child_value)

        return obj



class AbstractProvidedPortPrototypeBuilder:
    """Builder for AbstractProvidedPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractProvidedPortPrototype = AbstractProvidedPortPrototype()

    def build(self) -> AbstractProvidedPortPrototype:
        """Build and return AbstractProvidedPortPrototype object.

        Returns:
            AbstractProvidedPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
