"""PassThroughSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class PassThroughSwConnector(SwConnector):
    """AUTOSAR PassThroughSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided_outer: Optional[AbstractProvidedPortPrototype]
    required_outer: Optional[AbstractRequiredPortPrototype]
    def __init__(self) -> None:
        """Initialize PassThroughSwConnector."""
        super().__init__()
        self.provided_outer: Optional[AbstractProvidedPortPrototype] = None
        self.required_outer: Optional[AbstractRequiredPortPrototype] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PassThroughSwConnector":
        """Deserialize XML element to PassThroughSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PassThroughSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PassThroughSwConnector, cls).deserialize(element)

        # Parse provided_outer
        child = ARObject._find_child_element(element, "PROVIDED-OUTER")
        if child is not None:
            provided_outer_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.provided_outer = provided_outer_value

        # Parse required_outer
        child = ARObject._find_child_element(element, "REQUIRED-OUTER")
        if child is not None:
            required_outer_value = ARObject._deserialize_by_tag(child, "AbstractRequiredPortPrototype")
            obj.required_outer = required_outer_value

        return obj



class PassThroughSwConnectorBuilder:
    """Builder for PassThroughSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PassThroughSwConnector = PassThroughSwConnector()

    def build(self) -> PassThroughSwConnector:
        """Build and return PassThroughSwConnector object.

        Returns:
            PassThroughSwConnector instance
        """
        # TODO: Add validation
        return self._obj
