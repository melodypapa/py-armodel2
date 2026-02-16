"""SignalServiceTranslationElementProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class SignalServiceTranslationElementProps(Identifiable):
    """AUTOSAR SignalServiceTranslationElementProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # element
        "filter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataFilter,
        ),  # filter
        "transmission": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # transmission
    }

    def __init__(self) -> None:
        """Initialize SignalServiceTranslationElementProps."""
        super().__init__()
        self.element: Optional[DataPrototype] = None
        self.filter: Optional[DataFilter] = None
        self.transmission: Optional[Boolean] = None


class SignalServiceTranslationElementPropsBuilder:
    """Builder for SignalServiceTranslationElementProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationElementProps = SignalServiceTranslationElementProps()

    def build(self) -> SignalServiceTranslationElementProps:
        """Build and return SignalServiceTranslationElementProps object.

        Returns:
            SignalServiceTranslationElementProps instance
        """
        # TODO: Add validation
        return self._obj
