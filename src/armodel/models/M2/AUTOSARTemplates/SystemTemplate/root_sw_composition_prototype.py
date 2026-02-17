"""RootSwCompositionPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1003)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 186)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 240)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 18)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_map import (
    FlatMap,
)


class RootSwCompositionPrototype(Identifiable):
    """AUTOSAR RootSwCompositionPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "calibrations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (CalibrationParameter),
        ),  # calibrations
        "flat_map": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlatMap,
        ),  # flatMap
        "software": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompositionSwComponentType,
        ),  # software
    }

    def __init__(self) -> None:
        """Initialize RootSwCompositionPrototype."""
        super().__init__()
        self.calibrations: list[Any] = []
        self.flat_map: Optional[FlatMap] = None
        self.software: Optional[CompositionSwComponentType] = None


class RootSwCompositionPrototypeBuilder:
    """Builder for RootSwCompositionPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RootSwCompositionPrototype = RootSwCompositionPrototype()

    def build(self) -> RootSwCompositionPrototype:
        """Build and return RootSwCompositionPrototype object.

        Returns:
            RootSwCompositionPrototype instance
        """
        # TODO: Add validation
        return self._obj
