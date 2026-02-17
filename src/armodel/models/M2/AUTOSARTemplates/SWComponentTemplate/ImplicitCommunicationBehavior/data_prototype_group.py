"""DataPrototypeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 223)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataPrototypeGroup(Identifiable):
    """AUTOSAR DataPrototypeGroup."""

    data_prototype_group_group_in_composition_instance_refs: list[DataPrototypeGroup]
    implicit_datas: list[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize DataPrototypeGroup."""
        super().__init__()
        self.data_prototype_group_group_in_composition_instance_refs: list[DataPrototypeGroup] = []
        self.implicit_datas: list[VariableDataPrototype] = []


class DataPrototypeGroupBuilder:
    """Builder for DataPrototypeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeGroup = DataPrototypeGroup()

    def build(self) -> DataPrototypeGroup:
        """Build and return DataPrototypeGroup object.

        Returns:
            DataPrototypeGroup instance
        """
        # TODO: Add validation
        return self._obj
