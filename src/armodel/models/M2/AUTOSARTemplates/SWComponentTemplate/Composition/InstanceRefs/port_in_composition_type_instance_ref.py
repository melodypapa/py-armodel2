"""PortInCompositionTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 950)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class PortInCompositionTypeInstanceRef(ARObject):
    """AUTOSAR PortInCompositionTypeInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "abstract_context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwComponent),
        ),  # abstractContext
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompositionSwComponentType,
        ),  # base
        "target_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortPrototype,
        ),  # targetPort
    }

    def __init__(self) -> None:
        """Initialize PortInCompositionTypeInstanceRef."""
        super().__init__()
        self.abstract_context: Optional[Any] = None
        self.base: Optional[CompositionSwComponentType] = None
        self.target_port: Optional[PortPrototype] = None


class PortInCompositionTypeInstanceRefBuilder:
    """Builder for PortInCompositionTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInCompositionTypeInstanceRef = PortInCompositionTypeInstanceRef()

    def build(self) -> PortInCompositionTypeInstanceRef:
        """Build and return PortInCompositionTypeInstanceRef object.

        Returns:
            PortInCompositionTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
